import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
