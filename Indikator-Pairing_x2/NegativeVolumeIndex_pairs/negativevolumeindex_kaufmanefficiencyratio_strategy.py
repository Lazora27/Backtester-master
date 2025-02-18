import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_KaufmanEfficiencyRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und KaufmanEfficiencyRatio
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'KaufmanEfficiencyRatio': {
                'class': KaufmanEfficiencyRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KaufmanEfficiencyRatio'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'KaufmanEfficiencyRatio': 1.0
        })
    )
