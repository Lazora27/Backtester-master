import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
