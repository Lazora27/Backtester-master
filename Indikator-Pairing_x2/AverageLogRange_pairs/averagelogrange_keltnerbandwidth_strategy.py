import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
