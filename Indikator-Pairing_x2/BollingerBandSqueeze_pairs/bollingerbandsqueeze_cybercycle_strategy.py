import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und CyberCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'CyberCycle': 1.0
        })
    )
