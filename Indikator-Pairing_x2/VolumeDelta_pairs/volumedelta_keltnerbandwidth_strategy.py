import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
