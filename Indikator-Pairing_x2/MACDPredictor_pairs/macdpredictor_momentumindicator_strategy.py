import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MomentumIndicator': 1.0
        })
    )
