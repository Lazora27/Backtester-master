import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'BradleySiderograph': 1.0
        })
    )
