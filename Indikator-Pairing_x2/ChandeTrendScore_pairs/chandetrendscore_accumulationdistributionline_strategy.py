import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
