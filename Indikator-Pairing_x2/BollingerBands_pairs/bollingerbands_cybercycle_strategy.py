import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und CyberCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'CyberCycle': 1.0
        })
    )
