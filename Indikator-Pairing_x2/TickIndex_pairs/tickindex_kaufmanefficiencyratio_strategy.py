import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_KaufmanEfficiencyRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und KaufmanEfficiencyRatio
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'KaufmanEfficiencyRatio': {
                'class': KaufmanEfficiencyRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KaufmanEfficiencyRatio'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'KaufmanEfficiencyRatio': 1.0
        })
    )
