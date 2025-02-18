import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
