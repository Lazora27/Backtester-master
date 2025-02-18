import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und DPOCycles
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'DPOCycles': 1.0
        })
    )
