import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
