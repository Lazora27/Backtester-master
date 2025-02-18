import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'EhlersDecycler': 1.0
        })
    )
