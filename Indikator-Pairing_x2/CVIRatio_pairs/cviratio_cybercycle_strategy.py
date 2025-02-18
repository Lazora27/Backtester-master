import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und CyberCycle
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'CyberCycle': 1.0
        })
    )
