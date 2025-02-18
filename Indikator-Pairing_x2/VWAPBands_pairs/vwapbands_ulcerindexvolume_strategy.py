import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
