import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und CyberCycle
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'CyberCycle': 1.0
        })
    )
