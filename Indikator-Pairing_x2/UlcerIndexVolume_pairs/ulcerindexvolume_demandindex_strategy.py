import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und DemandIndex
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'DemandIndex': 1.0
        })
    )
