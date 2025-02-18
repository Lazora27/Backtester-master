import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und CyberCycle
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'CyberCycle': 1.0
        })
    )
