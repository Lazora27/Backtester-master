import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'MACDPredictor': 1.0
        })
    )
