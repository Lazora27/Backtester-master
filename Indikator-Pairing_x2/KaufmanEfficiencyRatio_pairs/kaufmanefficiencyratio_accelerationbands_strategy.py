import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KaufmanEfficiencyRatio_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KaufmanEfficiencyRatio und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'KaufmanEfficiencyRatio': {
                'class': KaufmanEfficiencyRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KaufmanEfficiencyRatio'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'KaufmanEfficiencyRatio': 1.0,
            'AccelerationBands': 1.0
        })
    )
