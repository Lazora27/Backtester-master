import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
