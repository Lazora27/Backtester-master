import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KaufmanEfficiencyRatio_NormalizedAverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KaufmanEfficiencyRatio und NormalizedAverageTrueRange
    """
    
    params = (
        ('indicators', {
            'KaufmanEfficiencyRatio': {
                'class': KaufmanEfficiencyRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KaufmanEfficiencyRatio'>
            },
            'NormalizedAverageTrueRange': {
                'class': NormalizedAverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedAverageTrueRange'>
            }
        }),
        ('weights', {
            'KaufmanEfficiencyRatio': 1.0,
            'NormalizedAverageTrueRange': 1.0
        })
    )
