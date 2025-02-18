import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
