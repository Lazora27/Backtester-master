import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und RateOfChange
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'RateOfChange': 1.0
        })
    )
