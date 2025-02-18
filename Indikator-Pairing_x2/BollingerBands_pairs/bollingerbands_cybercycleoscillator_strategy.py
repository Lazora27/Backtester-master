import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
