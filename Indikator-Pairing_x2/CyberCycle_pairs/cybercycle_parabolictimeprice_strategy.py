import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
