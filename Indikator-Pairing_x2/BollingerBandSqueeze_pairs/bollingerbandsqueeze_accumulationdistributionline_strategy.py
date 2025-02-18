import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
