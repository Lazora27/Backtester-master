import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und CyberCycle
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'CyberCycle': 1.0
        })
    )
