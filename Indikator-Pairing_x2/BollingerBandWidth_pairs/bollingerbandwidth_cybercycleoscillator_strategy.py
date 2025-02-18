import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
