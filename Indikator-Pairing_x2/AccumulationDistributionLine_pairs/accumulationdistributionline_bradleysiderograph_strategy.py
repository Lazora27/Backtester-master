import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'BradleySiderograph': 1.0
        })
    )
