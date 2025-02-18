import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
