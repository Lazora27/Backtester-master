import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
