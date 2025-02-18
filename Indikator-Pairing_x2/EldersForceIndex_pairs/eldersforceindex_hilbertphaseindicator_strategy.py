import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_HilbertPhaseIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und HilbertPhaseIndicator
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'HilbertPhaseIndicator': {
                'class': HilbertPhaseIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertPhaseIndicator'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'HilbertPhaseIndicator': 1.0
        })
    )
