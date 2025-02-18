import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_KaufmanEfficiencyRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und KaufmanEfficiencyRatio
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'KaufmanEfficiencyRatio': {
                'class': KaufmanEfficiencyRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KaufmanEfficiencyRatio'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'KaufmanEfficiencyRatio': 1.0
        })
    )
