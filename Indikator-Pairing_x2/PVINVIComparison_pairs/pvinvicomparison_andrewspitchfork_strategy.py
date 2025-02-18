import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
