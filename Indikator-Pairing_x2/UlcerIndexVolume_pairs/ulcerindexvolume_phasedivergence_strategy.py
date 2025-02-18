import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'PhaseDivergence': 1.0
        })
    )
