import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
