import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycleOscillator_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycleOscillator und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'CyberCycleOscillator': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
