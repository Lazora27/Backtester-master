import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'IchimokuCloud': 1.0
        })
    )
