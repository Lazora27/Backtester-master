import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
