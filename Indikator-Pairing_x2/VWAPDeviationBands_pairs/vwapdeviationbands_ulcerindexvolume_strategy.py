import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
