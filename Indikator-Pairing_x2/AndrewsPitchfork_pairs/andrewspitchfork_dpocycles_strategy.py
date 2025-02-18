import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'DPOCycles': 1.0
        })
    )
