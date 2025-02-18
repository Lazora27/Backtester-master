import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'UlcerIndex': 1.0
        })
    )
