import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
