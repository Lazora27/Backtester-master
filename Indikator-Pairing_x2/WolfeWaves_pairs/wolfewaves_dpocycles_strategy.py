import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und DPOCycles
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'DPOCycles': 1.0
        })
    )
