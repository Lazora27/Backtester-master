import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
