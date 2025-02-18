import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
