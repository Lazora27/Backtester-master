import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'EhlersDecycler': 1.0
        })
    )
