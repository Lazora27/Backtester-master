import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
