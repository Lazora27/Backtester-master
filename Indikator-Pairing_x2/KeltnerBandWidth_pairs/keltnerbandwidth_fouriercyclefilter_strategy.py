import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
