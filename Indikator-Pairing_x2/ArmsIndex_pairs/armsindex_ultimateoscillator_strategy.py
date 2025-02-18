import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'UltimateOscillator': 1.0
        })
    )
