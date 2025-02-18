import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
