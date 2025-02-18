import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
